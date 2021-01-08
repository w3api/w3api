---
title: Transform.addEventFilter()
permalink: Java/Transform-javafx-scene-transform/addEventFilter
date: 2021-01-04
key: JavaJava.T.Transform-javafx-scene-transform
category: java
tags: ['java se', 'javafx.scene.transform', 'javafx.graphics', 'metodo java', 'JavaFX 2.0']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.T.Transform-javafx-scene-transform.metodos valor="addEventFilter" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
<T extends Event>void addEventFilter(EventType<T> eventType, EventHandler<? super T> eventFilter)
~~~

## Parámetros
* **EventHandler&lt;? super T&gt; eventFilter**,  {% include w3api/param_description.html metodo=_data parametro="EventHandler<? super T> eventFilter" %}
* **EventType&lt;T&gt; eventType**,  {% include w3api/param_description.html metodo=_data parametro="EventType<T> eventType" %}

## Clase Padre
[Transform](/Java/Transform-javafx-scene-transform/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.T.Transform-javafx-scene-transform.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
