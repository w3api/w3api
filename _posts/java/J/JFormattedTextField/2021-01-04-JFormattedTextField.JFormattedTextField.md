---
title: JFormattedTextField.JFormattedTextField()
permalink: Java/JFormattedTextField/JFormattedTextField
date: 2021-01-04
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
* **Object currentValue**,  {% include w3api/param_description.html metodo=_data parametro="Object currentValue" %}
* **JFormattedTextField.AbstractFormatterFactory factory**,  {% include w3api/param_description.html metodo=_data parametro="JFormattedTextField.AbstractFormatterFactory factory" %}
* **JFormattedTextField.AbstractFormatter formatter**,  {% include w3api/param_description.html metodo=_data parametro="JFormattedTextField.AbstractFormatter formatter" %}
* **Format format**,  {% include w3api/param_description.html metodo=_data parametro="Format format" %}
* **Object value**,  {% include w3api/param_description.html metodo=_data parametro="Object value" %}

## Clase Padre
[JFormattedTextField](/Java/JFormattedTextField/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.J.JFormattedTextField.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
