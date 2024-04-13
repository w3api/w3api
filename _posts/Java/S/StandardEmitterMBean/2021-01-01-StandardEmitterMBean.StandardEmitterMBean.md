---
title: StandardEmitterMBean.StandardEmitterMBean()
permalink: /Java/StandardEmitterMBean/StandardEmitterMBean/
date: 2021-01-11
key: Java.S.StandardEmitterMBean
category: Java
tags: ['java se', 'javax.management', 'java.management', 'metodo java', 'Java 1.6']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.S.StandardEmitterMBean.constructores valor="StandardEmitterMBean" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
protected StandardEmitterMBean(Class<?> mbeanInterface, boolean isMXBean, NotificationEmitter emitter)
protected StandardEmitterMBean(Class<?> mbeanInterface, NotificationEmitter emitter)
public StandardEmitterMBean(T implementation, Class<T> mbeanInterface, boolean isMXBean, NotificationEmitter emitter)
public StandardEmitterMBean(T implementation, Class<T> mbeanInterface, NotificationEmitter emitter)
~~~

## Parámetros
* **boolean isMXBean**,  {% include w3api/param_description.html metodo=_dato parametro="boolean isMXBean" %}
* **Class&lt;T&gt; mbeanInterface**,  {% include w3api/param_description.html metodo=_dato parametro="Class<T> mbeanInterface" %}
* **NotificationEmitter emitter**,  {% include w3api/param_description.html metodo=_dato parametro="NotificationEmitter emitter" %}
* **Class&lt;?&gt; mbeanInterface**,  {% include w3api/param_description.html metodo=_dato parametro="Class<?> mbeanInterface" %}
* **T implementation**,  {% include w3api/param_description.html metodo=_dato parametro="T implementation" %}

## Excepciones
[IllegalArgumentException](/Java/IllegalArgumentException/)

## Clase Padre
[StandardEmitterMBean](/Java/StandardEmitterMBean/)

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
