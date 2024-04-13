---
title: SimpleMapProperty.SimpleMapProperty()
permalink: /Java/SimpleMapProperty/SimpleMapProperty/
date: 2021-01-11
key: Java.S.SimpleMapProperty
category: Java
tags: ['java se', 'javafx.beans.property', 'javafx.base', 'metodo java', 'JavaFX 2.1']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.S.SimpleMapProperty.constructores valor="SimpleMapProperty" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public SimpleMapProperty()
public SimpleMapProperty(Object bean, String name)
public SimpleMapProperty(Object bean, String name, ObservableMap<K,V> initialValue)
public SimpleMapProperty(ObservableMap<K,V> initialValue)
~~~

## Parámetros
* **String name**,  {% include w3api/param_description.html metodo=_dato parametro="String name" %}
* **ObservableMap&lt;K**,  {% include w3api/param_description.html metodo=_dato parametro="ObservableMap<K" %}
* **V&gt; initialValue**,  {% include w3api/param_description.html metodo=_dato parametro="V> initialValue" %}
* **Object bean**,  {% include w3api/param_description.html metodo=_dato parametro="Object bean" %}

## Clase Padre
[SimpleMapProperty](/Java/SimpleMapProperty/)

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
