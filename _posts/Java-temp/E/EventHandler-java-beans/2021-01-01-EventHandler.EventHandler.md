---
title: EventHandler.EventHandler()
permalink: /Java/EventHandler-java-beans/EventHandler/
date: 2021-01-11
key: Java.E.EventHandler-java-beans
category: Java
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
* **String action**,  {% include w3api/param_description.html metodo=_dato parametro="String action" %}
* **Object target**,  {% include w3api/param_description.html metodo=_dato parametro="Object target" %}
* **String eventPropertyName**,  {% include w3api/param_description.html metodo=_dato parametro="String eventPropertyName" %}
* **String listenerMethodName**,  {% include w3api/param_description.html metodo=_dato parametro="String listenerMethodName" %}

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
{%- for _ldc in _dato.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
