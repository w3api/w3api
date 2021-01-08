---
title: ObservableMap.addListener()
permalink: Java/ObservableMap/addListener
date: 2021-01-04
key: JavaJava.O.ObservableMap
category: java
tags: ['java se', 'javafx.collections', 'javafx.base', 'metodo java', 'JavaFX 2.0']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.O.ObservableMap.metodos valor="addListener" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
void addListener(MapChangeListener<? super K,? super V> listener)
~~~

## Parámetros
* **MapChangeListener&lt;? super K**,  {% include w3api/param_description.html metodo=_data parametro="MapChangeListener<? super K" %}
* **? super V&gt; listener**,  {% include w3api/param_description.html metodo=_data parametro="? super V> listener" %}

## Clase Padre
[ObservableMap](/Java/ObservableMap/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.O.ObservableMap.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
