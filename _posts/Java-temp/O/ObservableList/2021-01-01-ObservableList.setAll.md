---
title: ObservableList.setAll()
permalink: /Java/ObservableList/setAll/
date: 2021-01-11
key: Java.O.ObservableList
category: Java
tags: ['java se', 'javafx.collections', 'javafx.base', 'metodo java', 'JavaFX 2.0']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.O.ObservableList.metodos valor="setAll" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
boolean setAll(E... elements)
boolean setAll(Collection<? extends E> col)
~~~

## Parámetros
* **E... elements**,  {% include w3api/param_description.html metodo=_dato parametro="E... elements" %}
* **Collection&lt;? extends E&gt; col**,  {% include w3api/param_description.html metodo=_dato parametro="Collection<? extends E> col" %}

## Excepciones
[NullPointerException](/Java/NullPointerException/)

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
