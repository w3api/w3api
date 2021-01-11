---
title: JTextField.JTextField()
permalink: Java/JTextField/JTextField
date: 2021-01-11
key: JavaJava.J.JTextField
category: java
tags: ['java se', 'javax.swing', 'java.desktop', 'metodo java', 'Java 1.2']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.J.JTextField.constructores valor="JTextField" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public JTextField()
public JTextField(int columns)
public JTextField(String text)
public JTextField(String text, int columns)
public JTextField(Document doc, String text, int columns)
~~~

## Parámetros
* **String text**,  {% include w3api/param_description.html metodo=_dato parametro="String text" %}
* **int columns**,  {% include w3api/param_description.html metodo=_dato parametro="int columns" %}
* **Document doc**,  {% include w3api/param_description.html metodo=_dato parametro="Document doc" %}

## Excepciones
[IllegalArgumentException](/Java/IllegalArgumentException/)

## Clase Padre
[JTextField](/Java/JTextField/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in _dato.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
