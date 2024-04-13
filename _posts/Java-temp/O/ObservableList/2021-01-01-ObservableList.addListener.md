---
title: ObservableList.addListener()
permalink: /Java/ObservableList/addListener/
date: 2021-01-11
key: Java.O.ObservableList
category: Java
tags: ['java se', 'javafx.collections', 'javafx.base', 'metodo java', 'JavaFX 2.0']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.O.ObservableList.metodos valor="addListener" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
void addListener(ListChangeListener<? super E> listener)
~~~

## Parámetros
* **ListChangeListener&lt;? super E&gt; listener**,  {% include w3api/param_description.html metodo=_dato parametro="ListChangeListener<? super E> listener" %}

## Clase Padre
[ObservableList](/Java/ObservableList/)

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
