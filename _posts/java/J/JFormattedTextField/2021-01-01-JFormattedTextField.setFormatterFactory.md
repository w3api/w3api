---
title: JFormattedTextField.setFormatterFactory()
permalink: Java/JFormattedTextField/setFormatterFactory
date: 2021-01-11
key: JavaJava.J.JFormattedTextField
category: java
tags: ['java se', 'javax.swing', 'java.desktop', 'metodo java', 'Java 1.4']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.J.JFormattedTextField.metodos valor="setFormatterFactory" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
@BeanProperty(visualUpdate=true, description="AbstractFormatterFactory, responsible for returning an AbstractFormatter that can format the current value.") public void setFormatterFactory(JFormattedTextField.AbstractFormatterFactory tf)
~~~

## Parámetros
* **JFormattedTextField.AbstractFormatterFactory tf**,  {% include w3api/param_description.html metodo=_dato parametro="JFormattedTextField.AbstractFormatterFactory tf" %}

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
