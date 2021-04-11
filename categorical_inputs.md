#### Encodings of categorical variables

There seems to be two school of thoughts when it comes to one-hot encoding. Given a categorical variable, you have two choices:

- Use one-hot encoding. For example if the categories are (female, male), then your feature becomes either `[0, 1]` or `[0, 1]`.
- Represent them as multiple boolean features. If the categories are (female, male) then you end up having two features, each of them either `-1` or `1`. Such coding is called "effect coding" and is recommended over "dummy codding" which using `0` or `1`.



If categorical variables are to be mixed with continuous inputs, make sure to read `mixed_inputs.md`.

