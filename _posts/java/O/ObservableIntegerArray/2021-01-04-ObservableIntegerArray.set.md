---
title: ObservableIntegerArray.set()
permalink: Java/ObservableIntegerArray/set
date: 2021-01-04
key: JavaJava.O.ObservableIntegerArray
category: java
tags: ['java se', 'javafx.collections', 'javafx.base', 'metodo java', 'JavaFX 8.0']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.O.ObservableIntegerArray.metodos valor="set" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
void set(int index, int value)
void set(int destIndex, int[] src, int srcIndex, int length)
void set(int destIndex, ObservableIntegerArray src, int srcIndex, int length)
~~~

## Parámetros
* **int[] src**,  {% include w3api/param_description.html metodo=_data parametro="int[] src" %}
* **int destIndex**,  {% include w3api/param_description.html metodo=_data parametro="int destIndex" %}
* **ObservableIntegerArray src**,  {% include w3api/param_description.html metodo=_data parametro="ObservableIntegerArray src" %}
* **int srcIndex**,  {% include w3api/param_description.html metodo=_data parametro="int srcIndex" %}
* **int value**,  {% include w3api/param_description.html metodo=_data parametro="int value" %}
* **int length**,  {% include w3api/param_description.html metodo=_data parametro="int length" %}
* **int index**,  {% include w3api/param_description.html metodo=_data parametro="int index" %}

## Excepciones
[ArrayIndexOutOfBoundsException](/Java/ArrayIndexOutOfBoundsException/)

## Clase Padre
[ObservableIntegerArray](/Java/ObservableIntegerArray/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.O.ObservableIntegerArray.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
