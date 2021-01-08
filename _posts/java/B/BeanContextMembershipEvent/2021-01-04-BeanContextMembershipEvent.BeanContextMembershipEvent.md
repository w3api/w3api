---
title: BeanContextMembershipEvent.BeanContextMembershipEvent()
permalink: Java/BeanContextMembershipEvent/BeanContextMembershipEvent
date: 2021-01-04
key: JavaJava.B.BeanContextMembershipEvent
category: java
tags: ['java se', 'java.beans.beancontext', 'java.desktop', 'metodo java', 'Java 1.2']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.B.BeanContextMembershipEvent.constructores valor="BeanContextMembershipEvent" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public BeanContextMembershipEvent(BeanContext bc, Object[] changes)
public BeanContextMembershipEvent(BeanContext bc, Collection changes)
~~~

## Parámetros
* **Collection changes**,  {% include w3api/param_description.html metodo=_data parametro="Collection changes" %}
* **Object[] changes**,  {% include w3api/param_description.html metodo=_data parametro="Object[] changes" %}
* **BeanContext bc**,  {% include w3api/param_description.html metodo=_data parametro="BeanContext bc" %}

## Excepciones
[NullPointerException](/Java/NullPointerException/)

## Clase Padre
[BeanContextMembershipEvent](/Java/BeanContextMembershipEvent/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.B.BeanContextMembershipEvent.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
