---
title: ObservableArray.removeListener()
permalink: Java/ObservableArray/removeListener
date: 2021-01-11
key: JavaJava.O.ObservableArray
category: java
tags: ['java se', 'javafx.collections', 'javafx.base', 'metodo java', 'JavaFX 8.0']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.O.ObservableArray.metodos valor="removeListener" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
void removeListener(ArrayChangeListener<T> listener)
~~~

## Parámetros
* **ArrayChangeListener&lt;T&gt; listener**,  {% include w3api/param_description.html metodo=_dato parametro="ArrayChangeListener<T> listener" %}

## Excepciones
[NullPointerException](/Java/NullPointerException/)

## Clase Padre
[ObservableArray](/Java/ObservableArray/)

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
