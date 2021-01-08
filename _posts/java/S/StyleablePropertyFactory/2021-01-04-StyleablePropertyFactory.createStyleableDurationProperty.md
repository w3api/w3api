---
title: StyleablePropertyFactory.createStyleableDurationProperty()
permalink: Java/StyleablePropertyFactory/createStyleableDurationProperty
date: 2021-01-04
key: JavaJava.S.StyleablePropertyFactory
category: java
tags: ['java se', 'javafx.css', 'javafx.graphics', 'metodo java', 'JavaFX 8.0']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.S.StyleablePropertyFactory.metodos valor="createStyleableDurationProperty" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public final StyleableProperty<Duration> createStyleableDurationProperty(S styleable, String propertyName, String cssProperty)
public final StyleableProperty<Duration> createStyleableDurationProperty(S styleable, String propertyName, String cssProperty, Function<S,StyleableProperty<Duration>> function)
public final StyleableProperty<Duration> createStyleableDurationProperty(S styleable, String propertyName, String cssProperty, Function<S,StyleableProperty<Duration>> function, Duration initialValue)
public final StyleableProperty<Duration> createStyleableDurationProperty(S styleable, String propertyName, String cssProperty, Function<S,StyleableProperty<Duration>> function, Duration initialValue, boolean inherits)
~~~

## Parámetros
* **String cssProperty**,  {% include w3api/param_description.html metodo=_data parametro="String cssProperty" %}
* **Duration initialValue**,  {% include w3api/param_description.html metodo=_data parametro="Duration initialValue" %}
* **boolean inherits**,  {% include w3api/param_description.html metodo=_data parametro="boolean inherits" %}
* **String propertyName**,  {% include w3api/param_description.html metodo=_data parametro="String propertyName" %}
* **StyleableProperty&lt;Duration&gt;&gt; function**,  {% include w3api/param_description.html metodo=_data parametro="StyleableProperty<Duration>> function" %}
* **Function&lt;S**,  {% include w3api/param_description.html metodo=_data parametro="Function<S" %}
* **S styleable**,  {% include w3api/param_description.html metodo=_data parametro="S styleable" %}

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
{%- for _ldc in site.data.Java.S.StyleablePropertyFactory.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
