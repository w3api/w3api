---
title: DynamicMBean.invoke()
permalink: /Java/DynamicMBean/invoke/
date: 2021-01-11
key: Java.D.DynamicMBean
category: Java
tags: ['java se', 'javax.management', 'java.management', 'metodo java', 'Java 1.5']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.D.DynamicMBean.metodos valor="invoke" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
Object invoke(String actionName, Object[] params, String[] signature) throws MBeanException, ReflectionException
~~~

## Parámetros
* **String actionName**,  {% include w3api/param_description.html metodo=_dato parametro="String actionName" %}
* **Object[] params**,  {% include w3api/param_description.html metodo=_dato parametro="Object[] params" %}
* **String[] signature**,  {% include w3api/param_description.html metodo=_dato parametro="String[] signature" %}

## Excepciones
[ReflectionException](/Java/ReflectionException/), [MBeanException](/Java/MBeanException/)

## Clase Padre
[DynamicMBean](/Java/DynamicMBean/)

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
