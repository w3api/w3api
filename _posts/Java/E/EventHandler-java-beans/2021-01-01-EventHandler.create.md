---
title: EventHandler.create()
permalink: /Java/EventHandler-java-beans/create/
date: 2021-01-11
key: Java.E.EventHandler-java-beans
category: Java
tags: ['java se', 'java.beans', 'java.desktop', 'metodo java', 'Java 1.4']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.E.EventHandler-java-beans.metodos valor="create" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
static <T> T create(Class<T> listenerInterface, Object target, String action)
static <T> T create(Class<T> listenerInterface, Object target, String action, String eventPropertyName)
static <T> T create(Class<T> listenerInterface, Object target, String action, String eventPropertyName, String listenerMethodName)
~~~

## Parámetros
* **String action**,  {% include w3api/param_description.html metodo=_dato parametro="String action" %}
* **Class&lt;T&gt; listenerInterface**,  {% include w3api/param_description.html metodo=_dato parametro="Class<T> listenerInterface" %}
* **Object target**,  {% include w3api/param_description.html metodo=_dato parametro="Object target" %}
* **String listenerMethodName**,  {% include w3api/param_description.html metodo=_dato parametro="String listenerMethodName" %}
* **String eventPropertyName**,  {% include w3api/param_description.html metodo=_dato parametro="String eventPropertyName" %}

## Clase Padre
[EventHandler](/Java/EventHandler-java-beans/)

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
