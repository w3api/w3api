---
title: SizeSequence.insertEntries()
permalink: /Java/SizeSequence/insertEntries/
date: 2021-01-11
key: Java.S.SizeSequence
category: Java
tags: ['java se', 'javax.swing', 'java.desktop', 'metodo java', 'Java 1.3']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.S.SizeSequence.metodos valor="insertEntries" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public void insertEntries(int start, int length, int value)
~~~

## Parámetros
* **int value**,  {% include w3api/param_description.html metodo=_dato parametro="int value" %}
* **int start**,  {% include w3api/param_description.html metodo=_dato parametro="int start" %}
* **int length**,  {% include w3api/param_description.html metodo=_dato parametro="int length" %}

## Excepciones
[ArrayIndexOutOfBoundsException](/Java/ArrayIndexOutOfBoundsException/)

## Clase Padre
[SizeSequence](/Java/SizeSequence/)

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
