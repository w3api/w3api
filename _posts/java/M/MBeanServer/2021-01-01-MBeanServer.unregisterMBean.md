---
title: MBeanServer.unregisterMBean()
permalink: Java/MBeanServer/unregisterMBean
date: 2021-01-11
key: JavaJava.M.MBeanServer
category: Java
tags: ['java se', 'javax.management', 'java.management', 'metodo java', 'Java 1.5']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.M.MBeanServer.metodos valor="unregisterMBean" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
void unregisterMBean(ObjectName name) throws InstanceNotFoundException, MBeanRegistrationException
~~~

## Parámetros
* **ObjectName name**,  {% include w3api/param_description.html metodo=_dato parametro="ObjectName name" %}

## Excepciones
[RuntimeOperationsException](/Java/RuntimeOperationsException/), [MBeanRegistrationException](/Java/MBeanRegistrationException/), [RuntimeErrorException](/Java/RuntimeErrorException/), [InstanceNotFoundException](/Java/InstanceNotFoundException/), [RuntimeMBeanException](/Java/RuntimeMBeanException/)

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
