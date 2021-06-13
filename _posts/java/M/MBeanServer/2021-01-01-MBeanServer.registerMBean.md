---
title: MBeanServer.registerMBean()
permalink: Java/MBeanServer/registerMBean
date: 2021-01-11
key: JavaJava.M.MBeanServer
category: Java
tags: ['java se', 'javax.management', 'java.management', 'metodo java', 'Java 1.5']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.M.MBeanServer.metodos valor="registerMBean" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
ObjectInstance registerMBean(Object object, ObjectName name) throws InstanceAlreadyExistsException, MBeanRegistrationException, NotCompliantMBeanException
~~~

## Parámetros
* **ObjectName name**,  {% include w3api/param_description.html metodo=_dato parametro="ObjectName name" %}
* **Object object**,  {% include w3api/param_description.html metodo=_dato parametro="Object object" %}

## Excepciones
[RuntimeOperationsException](/Java/RuntimeOperationsException/), [MBeanRegistrationException](/Java/MBeanRegistrationException/), [RuntimeErrorException](/Java/RuntimeErrorException/), [RuntimeMBeanException](/Java/RuntimeMBeanException/), [NotCompliantMBeanException](/Java/NotCompliantMBeanException/), [InstanceAlreadyExistsException](/Java/InstanceAlreadyExistsException/)

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
