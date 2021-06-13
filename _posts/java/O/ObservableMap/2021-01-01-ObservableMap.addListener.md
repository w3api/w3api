---
title: ObservableMap.addListener()
permalink: /Java/ObservableMap/addListener/
date: 2021-01-11
key: Java.O.ObservableMap
category: Java
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
* **MapChangeListener&lt;? super K**,  {% include w3api/param_description.html metodo=_dato parametro="MapChangeListener<? super K" %}
* **? super V&gt; listener**,  {% include w3api/param_description.html metodo=_dato parametro="? super V> listener" %}

## Clase Padre
[ObservableMap](/Java/ObservableMap/)

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
