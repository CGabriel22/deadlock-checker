class DeadlockChecker:
    def __init__(self):
        self.existing_resources = []
        self.available_resources = []
        self.allocation_array = []
        self.requisition_array = []
        self.process = []
        self.zero = []
        self.certain_counter = 0

    def subtract_resources(self, i, resources, matrix, matrix2, zero):
        aux = matrix2[i - 1]
        aux2 = matrix[i - 1]
        previous_resources = resources
        res_aux = []
        res = []

        for i in range(0, len(resources)):
            valor = int(resources[i]) - int(aux[i])
            res_aux.append(str(valor))

        resources = res_aux

        for j in range(0, len(resources)):
            valor2 = int(previous_resources[j]) + int(aux2[j])
            res.append(str(valor2))

        matrix[i - 1] = res

        matrix[i - 1] = zero
        matrix2[i - 1] = zero

        return res

    def check_possibility(self, error_counter, index, item_counter, proccess, requisition_array, available_resources, allocation_array, rounded, zero):
        ultimo = 0
        ultima_linha = []

        for i in range(0, int(proccess[0])):
            for j in range(0, int(proccess[1])):
                if(allocation_array[i] != zero):
                    if(item_counter < int(proccess[1])):
                        if(int(requisition_array[i][j]) > int(available_resources[j])):
                            error_counter.append(0)
                            if(rounded < int(proccess[0])):
                                resultado = int(
                                    requisition_array[i][j]) - int(available_resources[j])
                                print("O processo p" + str(index) + " esta em espera e aguardando " +
                                      str(resultado) + " instancias de R" + str(j + 1))
                            else:
                                ultimo = index
                                ultima_linha = requisition_array[i]

                        else:
                            error_counter.append(1)

                    elif(item_counter == int(proccess[1])):
                        if(sum(error_counter) == int(proccess[1])):
                            print("P" + str(index))
                            available_resources = self.subtract_resources(
                                index,
                                available_resources,
                                allocation_array,
                                requisition_array,
                                zero
                            )

                        error_counter.clear()
                        index = index + 1
                        item_counter = 0

                    item_counter = item_counter + 1

        available_resources = self.subtract_resources(
            index,
            available_resources,
            allocation_array,
            requisition_array,
            zero
        )
        return [available_resources, ultimo, ultima_linha]

    def start(self):
        file = open("entrada.txt", "r")
        content = file.readlines()
        for l in range(len(content)):
            line = content[l].split()
            if(l == 0):
                self.process = line
            elif(l == 2):
                self.existing_resources = line
            elif(l == 4):
                self.available_resources = line
            elif(l in range(6, 6 + int(self.process[0]))):
                self.allocation_array.append(line)
            elif(l in range((6 + int(self.process[0]) + 1), ((6 + int(self.process[0]) + 1) + int(self.process[0])))):
                self.requisition_array.append(line)
        for i in range(0, int(self.process[1])):
            self.zero.append('0')
        print(f'Processos: {self.process[0]}')
        print(f'Numero de recursos: {self.process[1]}')
        print(f'Recursos existentes: {self.existing_resources}')
        print(f'Recursos disponiveis: {self.available_resources}')
        print('Matriz de alocacao de recursos por processo:')
        for i in self.allocation_array:
            print(i)
        print('Matriz de requisicao de recursos por processo:')
        for i in self.requisition_array:
            print(i)

        print("\n execucao das verificacoes: \n")

        item_counter = 0
        error_counter = []
        index = 1
        for i in range(0, int(self.process[0])):
            error_counter.clear()
            index = 1
            print(f'\n - execucao {i + 1}')
            response_list = self.check_possibility(
                error_counter,
                index,
                item_counter,
                self.process,
                self.requisition_array,
                self.available_resources,
                self.allocation_array,
                i + 1,
                self.zero
            )
            self.available_resources = response_list[0]

        if(response_list[2] != []):
            for i in range(0, int(self.process[1])):
                if(int(response_list[2][i]) > int(self.available_resources[i])):
                    result = int(response_list[2][i]) - \
                        int(self.available_resources[i])
                    print("O processo p" + str(response_list[1]) + " esta em espera e aguardando " +
                          str(result) + " instancias de R" + str(i + 1))


if __name__ == '__main__':
    deadlockChecker = DeadlockChecker()
    deadlockChecker.start()
