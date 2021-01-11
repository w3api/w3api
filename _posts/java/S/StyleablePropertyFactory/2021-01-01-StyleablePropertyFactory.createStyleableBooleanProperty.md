---
title: StyleablePropertyFactory.createStyleableBooleanProperty()
permalink: Java/StyleablePropertyFactory/createStyleableBooleanProperty
date: 2021-01-11
key: JavaJava.S.StyleablePropertyFactory
category: java
tags: ['java se', 'javafx.css', 'javafx.graphics', 'metodo java', 'JavaFX 8.0']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.S.StyleablePropertyFactory.metodos valor="createStyleableBooleanProperty" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public final StyleableProperty<Boolean> createStyleableBooleanProperty(S styleable, String propertyName, String cssProperty)
public final StyleableProperty<Boolean> createStyleableBooleanProperty(S styleable, String propertyName, String cssProperty, Function<S,StyleableProperty<Boolean>> function)
public final StyleableProperty<Boolean> createStyleableBooleanProperty(S styleable, String propertyName, String cssProperty, Function<S,StyleableProperty<Boolean>> function, boolean initialValue)
public final StyleableProperty<Boolean> createStyleableBooleanProperty(S styleable, String propertyName, String cssProperty, Function<S,StyleableProperty<Boolean>> function, boolean initialValue, boolean inherits)
~~~

## Parámetros
* **boolean initialValue**,  {% include w3api/param_description.html metodo=_dato parametro="boolean initialValue" %}
* **String cssProperty**,  {% include w3api/param_description.html metodo=_dato parametro="String cssProperty" %}
* **String propertyName**,  {% include w3api/param_description.html metodo=_dato parametro="String propertyName" %}
* **boolean inherits**,  {% include w3api/param_description.html metodo=_dato parametro="boolean inherits" %}
* **Function&lt;S**,  {% include w3api/param_description.html metodo=_dato parametro="Function<S" %}
* **StyleableProperty&lt;Boolean&gt;&gt; function**,  {% include w3api/param_description.html metodo=_dato parametro="StyleableProperty<Boolean>> function" %}
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
