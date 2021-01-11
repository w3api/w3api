---
title: AbstractDocument.getText()
permalink: Java/AbstractDocument/getText
date: 2021-01-10
key: JavaJava.A.AbstractDocument
category: java
tags: ['java se', 'javax.swing.text', 'java.desktop', 'metodo java', 'Java 1.0']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.A.AbstractDocument.metodos valor="getText" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public String getText(int offset, int length) throws BadLocationException
public void getText(int offset, int length, Segment txt) throws BadLocationException
~~~

## Parámetros
* **int offset**,  {% include w3api/param_description.html metodo=_dato parametro="int offset" %}
* **int length**,  {% include w3api/param_description.html metodo=_dato parametro="int length" %}
* **Segment txt**,  {% include w3api/param_description.html metodo=_dato parametro="Segment txt" %}

## Excepciones
[BadLocationException](/Java/BadLocationException/)

## Clase Padre
[AbstractDocument](/Java/AbstractDocument/)

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
