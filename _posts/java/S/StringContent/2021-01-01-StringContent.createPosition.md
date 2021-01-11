---
title: StringContent.createPosition()
permalink: Java/StringContent/createPosition
date: 2021-01-11
key: JavaJava.S.StringContent
category: java
tags: ['java se', 'javax.swing.text', 'java.desktop', 'metodo java', 'Java 1.0']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.S.StringContent.metodos valor="createPosition" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public Position createPosition(int offset) throws BadLocationException
~~~

## Parámetros
* **int offset**,  {% include w3api/param_description.html metodo=_dato parametro="int offset" %}

## Excepciones
[BadLocationException](/Java/BadLocationException/)

## Clase Padre
[StringContent](/Java/StringContent/)

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
