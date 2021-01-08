---
title: EventHandler.create()
permalink: Java/EventHandler-java-beans/create
date: 2021-01-04
key: JavaJava.E.EventHandler-java-beans
category: java
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
* **String listenerMethodName**,  {% include w3api/param_description.html metodo=_data parametro="String listenerMethodName" %}
* **String action**,  {% include w3api/param_description.html metodo=_data parametro="String action" %}
* **String eventPropertyName**,  {% include w3api/param_description.html metodo=_data parametro="String eventPropertyName" %}
* **Object target**,  {% include w3api/param_description.html metodo=_data parametro="Object target" %}
* **Class&lt;T&gt; listenerInterface**,  {% include w3api/param_description.html metodo=_data parametro="Class<T> listenerInterface" %}

## Clase Padre
[EventHandler](/Java/EventHandler-java-beans/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.E.EventHandler-java-beans.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
