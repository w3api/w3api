---
title: AbstractWriter.getText()
permalink: Java/AbstractWriter/getText
date: 2021-01-11
key: JavaJava.A.AbstractWriter
category: java
tags: ['java se', 'javax.swing.text', 'java.desktop', 'metodo java', 'Java 1.0']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.A.AbstractWriter.metodos valor="getText" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
protected String getText(Element elem) throws BadLocationException
~~~

## Parámetros
* **Element elem**,  {% include w3api/param_description.html metodo=_dato parametro="Element elem" %}

## Excepciones
[BadLocationException](/Java/BadLocationException/)

## Clase Padre
[AbstractWriter](/Java/AbstractWriter/)

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
