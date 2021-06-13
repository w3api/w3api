---
title: ObservableIntegerArray.setAll()
permalink: /Java/ObservableIntegerArray/setAll/
date: 2021-01-11
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
* **int... elements**,  {% include w3api/param_description.html metodo=_dato parametro="int... elements" %}
* **int length**,  {% include w3api/param_description.html metodo=_dato parametro="int length" %}
* **int[] src**,  {% include w3api/param_description.html metodo=_dato parametro="int[] src" %}
* **int srcIndex**,  {% include w3api/param_description.html metodo=_dato parametro="int srcIndex" %}
* **ObservableIntegerArray src**,  {% include w3api/param_description.html metodo=_dato parametro="ObservableIntegerArray src" %}

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
{%- for _ldc in _dato.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
