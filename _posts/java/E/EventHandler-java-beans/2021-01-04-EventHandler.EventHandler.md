---
title: EventHandler.EventHandler()
permalink: Java/EventHandler-java-beans/EventHandler
date: 2021-01-04
key: JavaJava.E.EventHandler-java-beans
category: java
tags: ['java se', 'java.beans', 'java.desktop', 'metodo java', 'Java 1.4']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.E.EventHandler-java-beans.constructores valor="EventHandler" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
@ConstructorProperties({"target","action","eventPropertyName","listenerMethodName"}) public EventHandler(Object target, String action, String eventPropertyName, String listenerMethodName)
~~~

## Parámetros
* **Object target**,  {% include w3api/param_description.html metodo=_data parametro="Object target" %}
* **String action**,  {% include w3api/param_description.html metodo=_data parametro="String action" %}
* **String eventPropertyName**,  {% include w3api/param_description.html metodo=_data parametro="String eventPropertyName" %}
* **String listenerMethodName**,  {% include w3api/param_description.html metodo=_data parametro="String listenerMethodName" %}

## Excepciones
[NullPointerException](/Java/NullPointerException/)

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
