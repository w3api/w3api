---
title: MapExpression.valueAt()
permalink: /Java/MapExpression/valueAt/
date: 2021-01-11
key: Java.M.MapExpression
category: Java
tags: ['java se', 'javafx.beans.binding', 'javafx.base', 'metodo java', 'JavaFX 2.1']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.M.MapExpression.metodos valor="valueAt" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public ObjectBinding<V> valueAt(ObservableValue<K> key)
public ObjectBinding<V> valueAt(K key)
~~~

## Parámetros
* **K key**,  {% include w3api/param_description.html metodo=_dato parametro="K key" %}
* **ObservableValue&lt;K&gt; key**,  {% include w3api/param_description.html metodo=_dato parametro="ObservableValue<K> key" %}

## Excepciones
[NullPointerException](/Java/NullPointerException/)

## Clase Padre
[MapExpression](/Java/MapExpression/)

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
