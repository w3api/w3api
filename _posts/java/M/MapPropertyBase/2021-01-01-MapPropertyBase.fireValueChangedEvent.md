---
title: MapPropertyBase.fireValueChangedEvent()
permalink: /Java/MapPropertyBase/fireValueChangedEvent/
date: 2021-01-11
key: Java.M.MapPropertyBase
category: Java
tags: ['java se', 'javafx.beans.property', 'javafx.base', 'metodo java', 'JavaFX 2.1']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.M.MapPropertyBase.metodos valor="fireValueChangedEvent" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
protected void fireValueChangedEvent()
protected void fireValueChangedEvent(MapChangeListener.Change<? extends K,? extends V> change)
~~~

## Parámetros
* **MapChangeListener.Change&lt;? extends K**,  {% include w3api/param_description.html metodo=_dato parametro="MapChangeListener.Change<? extends K" %}
* **? extends V&gt; change**,  {% include w3api/param_description.html metodo=_dato parametro="? extends V> change" %}

## Clase Padre
[MapPropertyBase](/Java/MapPropertyBase/)

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
