---
title: ReadOnlyMapProperty.bindContent()
permalink: Java/ReadOnlyMapProperty/bindContent
date: 2021-01-11
key: JavaJava.R.ReadOnlyMapProperty
category: java
tags: ['java se', 'javafx.beans.property', 'javafx.base', 'metodo java', 'JavaFX 2.1']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.R.ReadOnlyMapProperty.metodos valor="bindContent" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public void bindContent(ObservableMap<K,V> map)
~~~

## Parámetros
* **ObservableMap&lt;K**,  {% include w3api/param_description.html metodo=_dato parametro="ObservableMap<K" %}
* **V&gt; map**,  {% include w3api/param_description.html metodo=_dato parametro="V> map" %}

## Excepciones
[IllegalArgumentException](/Java/IllegalArgumentException/), [NullPointerException](/Java/NullPointerException/)

## Clase Padre
[ReadOnlyMapProperty](/Java/ReadOnlyMapProperty/)

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
