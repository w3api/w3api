---
title: RMIConnection.setAttribute()
permalink: /Java/RMIConnection/setAttribute/
date: 2021-01-11
key: Java.R.RMIConnection
category: Java
tags: ['java se', 'javax.management.remote.rmi', 'java.management.rmi', 'metodo java', 'Java 1.5']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.R.RMIConnection.metodos valor="setAttribute" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
void setAttribute(ObjectName name, MarshalledObject attribute, Subject delegationSubject) throws InstanceNotFoundException, AttributeNotFoundException, InvalidAttributeValueException, MBeanException, ReflectionException, IOException
~~~

## Parámetros
* **ObjectName name**,  {% include w3api/param_description.html metodo=_dato parametro="ObjectName name" %}
* **MarshalledObject attribute**,  {% include w3api/param_description.html metodo=_dato parametro="MarshalledObject attribute" %}
* **Subject delegationSubject**,  {% include w3api/param_description.html metodo=_dato parametro="Subject delegationSubject" %}

## Excepciones
[InvalidAttributeValueException](/Java/InvalidAttributeValueException/), [RuntimeOperationsException](/Java/RuntimeOperationsException/), [IOException](/Java/IOException/), [ReflectionException](/Java/ReflectionException/), [SecurityException](/Java/SecurityException/), [AttributeNotFoundException](/Java/AttributeNotFoundException/), [MBeanException](/Java/MBeanException/), [InstanceNotFoundException](/Java/InstanceNotFoundException/)

## Clase Padre
[RMIConnection](/Java/RMIConnection/)

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
