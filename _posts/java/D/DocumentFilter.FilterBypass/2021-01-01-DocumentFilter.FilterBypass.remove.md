---
title: DocumentFilter.FilterBypass.remove()
permalink: Java/DocumentFilter/FilterBypass/remove
date: 2021-01-11
key: JavaJava.D.DocumentFilter.FilterBypass
category: java
tags: ['java se', 'javax.swing.text', 'java.desktop', 'metodo java', 'Java 1.4']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.D.DocumentFilter.FilterBypass.metodos valor="remove" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public abstract void remove(int offset, int length) throws BadLocationException
~~~

## Parámetros
* **int length**,  {% include w3api/param_description.html metodo=_dato parametro="int length" %}
* **int offset**,  {% include w3api/param_description.html metodo=_dato parametro="int offset" %}

## Excepciones
[BadLocationException](/Java/BadLocationException/)

## Clase Padre
[DocumentFilter.FilterBypass](/Java/DocumentFilter/FilterBypass/)

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
