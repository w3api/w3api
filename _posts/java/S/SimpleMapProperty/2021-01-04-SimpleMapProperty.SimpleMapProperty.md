---
title: SimpleMapProperty.SimpleMapProperty()
permalink: Java/SimpleMapProperty/SimpleMapProperty
date: 2021-01-04
key: JavaJava.S.SimpleMapProperty
category: java
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
* **Object bean**,  {% include w3api/param_description.html metodo=_data parametro="Object bean" %}
* **ObservableMap&lt;K**,  {% include w3api/param_description.html metodo=_data parametro="ObservableMap<K" %}
* **V&gt; initialValue**,  {% include w3api/param_description.html metodo=_data parametro="V> initialValue" %}
* **String name**,  {% include w3api/param_description.html metodo=_data parametro="String name" %}

## Clase Padre
[SimpleMapProperty](/Java/SimpleMapProperty/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.S.SimpleMapProperty.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
