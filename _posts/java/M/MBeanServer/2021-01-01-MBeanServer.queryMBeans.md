---
title: MBeanServer.queryMBeans()
permalink: /Java/MBeanServer/queryMBeans/
date: 2021-01-11
key: Java.M.MBeanServer
category: Java
tags: ['java se', 'javax.management', 'java.management', 'metodo java', 'Java 1.5']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.M.MBeanServer.metodos valor="queryMBeans" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
Set<ObjectInstance> queryMBeans(ObjectName name, QueryExp query)
~~~

## Parámetros
* **ObjectName name**,  {% include w3api/param_description.html metodo=_dato parametro="ObjectName name" %}
* **QueryExp query**,  {% include w3api/param_description.html metodo=_dato parametro="QueryExp query" %}

## Excepciones
[RuntimeOperationsException](/Java/RuntimeOperationsException/)

## Clase Padre
[MBeanServer](/Java/MBeanServer/)

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
