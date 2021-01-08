---
title: AbstractDocument.Content.remove()
permalink: Java/AbstractDocument/Content/remove
date: 2021-01-04
key: JavaJava.A.AbstractDocument.Content
category: java
tags: ['java se', 'javax.swing.text', 'java.desktop', 'metodo java', 'Java 1.0']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.A.AbstractDocument.Content.metodos valor="remove" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
UndoableEdit remove(int where, int nitems) throws BadLocationException
~~~

## Parámetros
* **int where**,  {% include w3api/param_description.html metodo=_data parametro="int where" %}
* **int nitems**,  {% include w3api/param_description.html metodo=_data parametro="int nitems" %}

## Excepciones
[BadLocationException](/Java/BadLocationException/)

## Clase Padre
[AbstractDocument.Content](/Java/AbstractDocument/Content/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.A.AbstractDocument.Content.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
