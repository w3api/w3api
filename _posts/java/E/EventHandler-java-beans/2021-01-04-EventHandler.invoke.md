---
title: EventHandler.invoke()
permalink: Java/EventHandler-java-beans/invoke
date: 2021-01-04
key: JavaJava.E.EventHandler-java-beans
category: java
tags: ['java se', 'java.beans', 'java.desktop', 'metodo java', 'Java 1.4']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.E.EventHandler-java-beans.metodos valor="invoke" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public Object invoke(Object proxy, Method method, Object[] arguments)
~~~

## Parámetros
* **Method method**,  {% include w3api/param_description.html metodo=_data parametro="Method method" %}
* **Object proxy**,  {% include w3api/param_description.html metodo=_data parametro="Object proxy" %}
* **Object[] arguments**,  {% include w3api/param_description.html metodo=_data parametro="Object[] arguments" %}

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
