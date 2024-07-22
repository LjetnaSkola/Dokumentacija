def foo(duplicate_list):
        new_list = list(set(duplicate_list))
        return new_list

def main():
        l = [1,2,2,3,4,5,4]
        print(f"Old list: {l}\nNew list: {foo(l)}")


if __name__ == "__main__":
    main()
