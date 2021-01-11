---
title: JFormattedTextField.JFormattedTextField()
permalink: Java/JFormattedTextField/JFormattedTextField
date: 2021-01-11
key: JavaJava.J.JFormattedTextField
category: java
tags: ['java se', 'javax.swing', 'java.desktop', 'metodo java', 'Java 1.4']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.J.JFormattedTextField.constructores valor="JFormattedTextField" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public JFormattedTextField()
public JFormattedTextField(Object value)
public JFormattedTextField(Format format)
public JFormattedTextField(JFormattedTextField.AbstractFormatter formatter)
public JFormattedTextField(JFormattedTextField.AbstractFormatterFactory factory)
public JFormattedTextField(JFormattedTextField.AbstractFormatterFactory factory, Object currentValue)
~~~

## Parámetros
* **JFormattedTextField.AbstractFormatter formatter**,  {% include w3api/param_description.html metodo=_dato parametro="JFormattedTextField.AbstractFormatter formatter" %}
* **JFormattedTextField.AbstractFormatterFactory factory**,  {% include w3api/param_description.html metodo=_dato parametro="JFormattedTextField.AbstractFormatterFactory factory" %}
* **Object value**,  {% include w3api/param_description.html metodo=_dato parametro="Object value" %}
* **Object currentValue**,  {% include w3api/param_description.html metodo=_dato parametro="Object currentValue" %}
* **Format format**,  {% include w3api/param_description.html metodo=_dato parametro="Format format" %}

## Clase Padre
[JFormattedTextField](/Java/JFormattedTextField/)

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
