---
title: StyleablePropertyFactory.createEffectCssMetaData()
permalink: Java/StyleablePropertyFactory/createEffectCssMetaData
date: 2021-01-04
key: JavaJava.S.StyleablePropertyFactory
category: java
tags: ['java se', 'javafx.css', 'javafx.graphics', 'metodo java', 'JavaFX 8.0']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.S.StyleablePropertyFactory.metodos valor="createEffectCssMetaData" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
<E extends Effect>CssMetaData<S,E> createEffectCssMetaData(String property, Function<S,StyleableProperty<E>> function)
<E extends Effect>CssMetaData<S,E> createEffectCssMetaData(String property, Function<S,StyleableProperty<E>> function, E initialValue)
<E extends Effect>CssMetaData<S,E> createEffectCssMetaData(String property, Function<S,StyleableProperty<E>> function, E initialValue, boolean inherits)
~~~

## Parámetros
* **StyleableProperty&lt;E&gt;&gt; function**,  {% include w3api/param_description.html metodo=_data parametro="StyleableProperty<E>> function" %}
* **boolean inherits**,  {% include w3api/param_description.html metodo=_data parametro="boolean inherits" %}
* **E initialValue**,  {% include w3api/param_description.html metodo=_data parametro="E initialValue" %}
* **Function&lt;S**,  {% include w3api/param_description.html metodo=_data parametro="Function<S" %}
* **String property**,  {% include w3api/param_description.html metodo=_data parametro="String property" %}

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
