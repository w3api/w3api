---
title: ItemEvent.ItemEvent()
permalink: /Java/ItemEvent/ItemEvent/
date: 2021-01-11
key: Java.I.ItemEvent
category: Java
tags: ['java se', 'java.awt.event', 'java.desktop', 'metodo java', 'Java 1.1']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.I.ItemEvent.constructores valor="ItemEvent" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public ItemEvent(ItemSelectable source, int id, Object item, int stateChange)
~~~

## Parámetros
* **ItemSelectable source**,  {% include w3api/param_description.html metodo=_dato parametro="ItemSelectable source" %}
* **int id**,  {% include w3api/param_description.html metodo=_dato parametro="int id" %}
* **Object item**,  {% include w3api/param_description.html metodo=_dato parametro="Object item" %}
* **int stateChange**,  {% include w3api/param_description.html metodo=_dato parametro="int stateChange" %}

## Excepciones
[IllegalArgumentException](/Java/IllegalArgumentException/)

## Clase Padre
[ItemEvent](/Java/ItemEvent/)

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
