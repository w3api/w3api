---
title: StyleablePropertyFactory.createStyleablePaintProperty()
permalink: /Java/StyleablePropertyFactory/createStyleablePaintProperty/
date: 2021-01-11
key: Java.S.StyleablePropertyFactory
category: Java
tags: ['java se', 'javafx.css', 'javafx.graphics', 'metodo java', 'JavaFX 8.0']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.S.StyleablePropertyFactory.metodos valor="createStyleablePaintProperty" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public final StyleableProperty<Paint> createStyleablePaintProperty(S styleable, String propertyName, String cssProperty)
public final StyleableProperty<Paint> createStyleablePaintProperty(S styleable, String propertyName, String cssProperty, Function<S,StyleableProperty<Paint>> function)
public final StyleableProperty<Paint> createStyleablePaintProperty(S styleable, String propertyName, String cssProperty, Function<S,StyleableProperty<Paint>> function, Paint initialValue)
public final StyleableProperty<Paint> createStyleablePaintProperty(S styleable, String propertyName, String cssProperty, Function<S,StyleableProperty<Paint>> function, Paint initialValue, boolean inherits)
~~~

## Parámetros
* **Paint initialValue**,  {% include w3api/param_description.html metodo=_dato parametro="Paint initialValue" %}
* **String cssProperty**,  {% include w3api/param_description.html metodo=_dato parametro="String cssProperty" %}
* **StyleableProperty&lt;Paint&gt;&gt; function**,  {% include w3api/param_description.html metodo=_dato parametro="StyleableProperty<Paint>> function" %}
* **String propertyName**,  {% include w3api/param_description.html metodo=_dato parametro="String propertyName" %}
* **boolean inherits**,  {% include w3api/param_description.html metodo=_dato parametro="boolean inherits" %}
* **Function&lt;S**,  {% include w3api/param_description.html metodo=_dato parametro="Function<S" %}
* **S styleable**,  {% include w3api/param_description.html metodo=_dato parametro="S styleable" %}

## Excepciones
[NoSuchElementException](/Java/NoSuchElementException/), [IllegalArgumentException](/Java/IllegalArgumentException/)

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
