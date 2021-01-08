---
title: ObservableIntegerArray.setAll()
permalink: Java/ObservableIntegerArray/setAll
date: 2021-01-04
key: JavaJava.O.ObservableIntegerArray
category: java
tags: ['java se', 'javafx.collections', 'javafx.base', 'metodo java', 'JavaFX 8.0']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.O.ObservableIntegerArray.metodos valor="setAll" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
void setAll(int... elements)
void setAll(int[] src, int srcIndex, int length)
void setAll(ObservableIntegerArray src)
void setAll(ObservableIntegerArray src, int srcIndex, int length)
~~~

## Parámetros
* **int[] src**,  {% include w3api/param_description.html metodo=_data parametro="int[] src" %}
* **ObservableIntegerArray src**,  {% include w3api/param_description.html metodo=_data parametro="ObservableIntegerArray src" %}
* **int srcIndex**,  {% include w3api/param_description.html metodo=_data parametro="int srcIndex" %}
* **int length**,  {% include w3api/param_description.html metodo=_data parametro="int length" %}
* **int... elements**,  {% include w3api/param_description.html metodo=_data parametro="int... elements" %}

## Excepciones
[NullPointerException](/Java/NullPointerException/)

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
