---
title: ReadOnlyListProperty.bindContent()
permalink: Java/ReadOnlyListProperty/bindContent
date: 2021-01-11
key: JavaJava.R.ReadOnlyListProperty
category: java
tags: ['java se', 'javafx.beans.property', 'javafx.base', 'metodo java', 'JavaFX 2.1']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.R.ReadOnlyListProperty.metodos valor="bindContent" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public void bindContent(ObservableList<E> list)
~~~

## Parámetros
* **ObservableList&lt;E&gt; list**,  {% include w3api/param_description.html metodo=_dato parametro="ObservableList<E> list" %}

## Excepciones
[IllegalArgumentException](/Java/IllegalArgumentException/), [NullPointerException](/Java/NullPointerException/)

## Clase Padre
[ReadOnlyListProperty](/Java/ReadOnlyListProperty/)

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