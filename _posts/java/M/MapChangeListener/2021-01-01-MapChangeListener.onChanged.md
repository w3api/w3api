---
title: MapChangeListener.onChanged()
permalink: /Java/MapChangeListener/onChanged/
date: 2021-01-11
key: Java.M.MapChangeListener
category: Java
tags: ['java se', 'javafx.collections', 'javafx.base', 'metodo java', 'JavaFX 2.0']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.M.MapChangeListener.metodos valor="onChanged" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
void onChanged(MapChangeListener.Change<? extends K,? extends V> change)
~~~

## Parámetros
* **MapChangeListener.Change&lt;? extends K**,  {% include w3api/param_description.html metodo=_dato parametro="MapChangeListener.Change<? extends K" %}
* **? extends V&gt; change**,  {% include w3api/param_description.html metodo=_dato parametro="? extends V> change" %}

## Clase Padre
[MapChangeListener](/Java/MapChangeListener/)

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
