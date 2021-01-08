---
title: AbstractDocument.remove()
permalink: Java/AbstractDocument/remove
date: 2021-01-04
key: JavaJava.A.AbstractDocument
category: java
tags: ['java se', 'javax.swing.text', 'java.desktop', 'metodo java', 'Java 1.0']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.A.AbstractDocument.metodos valor="remove" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public void remove(int offs, int len) throws BadLocationException
~~~

## Parámetros
* **int len**,  {% include w3api/param_description.html metodo=_data parametro="int len" %}
* **int offs**,  {% include w3api/param_description.html metodo=_data parametro="int offs" %}

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
{%- for _ldc in site.data.Java.A.AbstractDocument.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
