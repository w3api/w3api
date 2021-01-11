---
title: StyleablePropertyFactory.createStyleableEnumProperty()
permalink: Java/StyleablePropertyFactory/createStyleableEnumProperty
date: 2021-01-11
key: JavaJava.S.StyleablePropertyFactory
category: java
tags: ['java se', 'javafx.css', 'javafx.graphics', 'metodo java', 'JavaFX 8.0']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.S.StyleablePropertyFactory.metodos valor="createStyleableEnumProperty" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
<E extends Enum<E>>StyleableProperty<E> createStyleableEnumProperty(S styleable, String propertyName, String cssProperty, Function<S,StyleableProperty<E>> function, Class<E> enumClass)
<E extends Enum<E>>StyleableProperty<E> createStyleableEnumProperty(S styleable, String propertyName, String cssProperty, Function<S,StyleableProperty<E>> function, Class<E> enumClass, E initialValue)
<E extends Enum<E>>StyleableProperty<E> createStyleableEnumProperty(S styleable, String propertyName, String cssProperty, Function<S,StyleableProperty<E>> function, Class<E> enumClass, E initialValue, boolean inherits)
~~~

## Parámetros
* **Class&lt;E&gt; enumClass**,  {% include w3api/param_description.html metodo=_dato parametro="Class<E> enumClass" %}
* **String cssProperty**,  {% include w3api/param_description.html metodo=_dato parametro="String cssProperty" %}
* **StyleableProperty&lt;E&gt;&gt; function**,  {% include w3api/param_description.html metodo=_dato parametro="StyleableProperty<E>> function" %}
* **String propertyName**,  {% include w3api/param_description.html metodo=_dato parametro="String propertyName" %}
* **boolean inherits**,  {% include w3api/param_description.html metodo=_dato parametro="boolean inherits" %}
* **E initialValue**,  {% include w3api/param_description.html metodo=_dato parametro="E initialValue" %}
* **Function&lt;S**,  {% include w3api/param_description.html metodo=_dato parametro="Function<S" %}
* **S styleable**,  {% include w3api/param_description.html metodo=_dato parametro="S styleable" %}

## Clase Padre
[StyleablePropertyFactory](/Java/StyleablePropertyFactory/)

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
