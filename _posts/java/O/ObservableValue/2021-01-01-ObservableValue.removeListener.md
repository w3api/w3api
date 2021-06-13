---
title: ObservableValue.removeListener()
permalink: /Java/ObservableValue/removeListener/
date: 2021-01-11
key: Java.O.ObservableValue
category: Java
tags: ['java se', 'javafx.beans.value', 'javafx.base', 'metodo java', 'JavaFX 2.0']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.O.ObservableValue.metodos valor="removeListener" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
void removeListener(ChangeListener<? super T> listener)
~~~

## Parámetros
* **ChangeListener&lt;? super T&gt; listener**,  {% include w3api/param_description.html metodo=_dato parametro="ChangeListener<? super T> listener" %}

## Excepciones
[NullPointerException](/Java/NullPointerException/)

## Clase Padre
[ObservableValue](/Java/ObservableValue/)

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
