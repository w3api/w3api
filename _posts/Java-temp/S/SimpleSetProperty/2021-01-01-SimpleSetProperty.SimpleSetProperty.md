---
title: SimpleSetProperty.SimpleSetProperty()
permalink: /Java/SimpleSetProperty/SimpleSetProperty/
date: 2021-01-11
key: Java.S.SimpleSetProperty
category: Java
tags: ['java se', 'javafx.beans.property', 'javafx.base', 'metodo java', 'JavaFX 2.1']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.S.SimpleSetProperty.constructores valor="SimpleSetProperty" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public SimpleSetProperty()
public SimpleSetProperty(Object bean, String name)
public SimpleSetProperty(Object bean, String name, ObservableSet<E> initialValue)
public SimpleSetProperty(ObservableSet<E> initialValue)
~~~

## Parámetros
* **String name**,  {% include w3api/param_description.html metodo=_dato parametro="String name" %}
* **ObservableSet&lt;E&gt; initialValue**,  {% include w3api/param_description.html metodo=_dato parametro="ObservableSet<E> initialValue" %}
* **Object bean**,  {% include w3api/param_description.html metodo=_dato parametro="Object bean" %}

## Clase Padre
[SimpleSetProperty](/Java/SimpleSetProperty/)

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
