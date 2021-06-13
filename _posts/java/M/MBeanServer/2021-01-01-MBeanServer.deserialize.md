---
title: MBeanServer.deserialize()
permalink: /Java/MBeanServer/deserialize/
date: 2021-01-11
key: Java.M.MBeanServer
category: Java
tags: ['java se', 'javax.management', 'java.management', 'metodo java', 'Java 1.5']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.M.MBeanServer.metodos valor="deserialize" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
@Deprecated(since="1.5") default ObjectInputStream deserialize(String className, byte[] data) throws OperationsException, ReflectionException
@Deprecated(since="1.5") default ObjectInputStream deserialize(String className, ObjectName loaderName, byte[] data) throws InstanceNotFoundException, OperationsException, ReflectionException
@Deprecated(since="1.5") default ObjectInputStream deserialize(ObjectName name, byte[] data) throws InstanceNotFoundException, OperationsException
~~~

## Parámetros
* **ObjectName name**,  {% include w3api/param_description.html metodo=_dato parametro="ObjectName name" %}
* **byte[] data**,  {% include w3api/param_description.html metodo=_dato parametro="byte[] data" %}
* **ObjectName loaderName**,  {% include w3api/param_description.html metodo=_dato parametro="ObjectName loaderName" %}
* **String className**,  {% include w3api/param_description.html metodo=_dato parametro="String className" %}

## Excepciones
[OperationsException](/Java/OperationsException/), [InstanceNotFoundException](/Java/InstanceNotFoundException/), [ReflectionException](/Java/ReflectionException/)

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
