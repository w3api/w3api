---
title: SimpleListProperty.SimpleListProperty()
permalink: Java/SimpleListProperty/SimpleListProperty
date: 2021-01-11
key: JavaJava.S.SimpleListProperty
category: java
tags: ['java se', 'javafx.beans.property', 'javafx.base', 'metodo java', 'JavaFX 2.1']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.S.SimpleListProperty.constructores valor="SimpleListProperty" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public SimpleListProperty()
public SimpleListProperty(Object bean, String name)
public SimpleListProperty(Object bean, String name, ObservableList<E> initialValue)
public SimpleListProperty(ObservableList<E> initialValue)
~~~

## Parámetros
* **String name**,  {% include w3api/param_description.html metodo=_dato parametro="String name" %}
* **ObservableList&lt;E&gt; initialValue**,  {% include w3api/param_description.html metodo=_dato parametro="ObservableList<E> initialValue" %}
* **Object bean**,  {% include w3api/param_description.html metodo=_dato parametro="Object bean" %}

## Clase Padre
[SimpleListProperty](/Java/SimpleListProperty/)

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
