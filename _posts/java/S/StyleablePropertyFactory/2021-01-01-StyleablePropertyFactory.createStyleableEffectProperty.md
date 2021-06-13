---
title: StyleablePropertyFactory.createStyleableEffectProperty()
permalink: /Java/StyleablePropertyFactory/createStyleableEffectProperty/
date: 2021-01-11
key: Java.S.StyleablePropertyFactory
category: Java
tags: ['java se', 'javafx.css', 'javafx.graphics', 'metodo java', 'JavaFX 8.0']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.S.StyleablePropertyFactory.metodos valor="createStyleableEffectProperty" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public final StyleableProperty<Effect> createStyleableEffectProperty(S styleable, String propertyName, String cssProperty)
<E extends Enum<E>>StyleableProperty<E> createStyleableEffectProperty(S styleable, String propertyName, String cssProperty, Class<E> enumClass)
<E extends Effect>StyleableProperty<E> createStyleableEffectProperty(S styleable, String propertyName, String cssProperty, Function<S,StyleableProperty<E>> function)
<E extends Effect>StyleableProperty<E> createStyleableEffectProperty(S styleable, String propertyName, String cssProperty, Function<S,StyleableProperty<E>> function, E initialValue)
<E extends Effect>StyleableProperty<E> createStyleableEffectProperty(S styleable, String propertyName, String cssProperty, Function<S,StyleableProperty<E>> function, E initialValue, boolean inherits)
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
